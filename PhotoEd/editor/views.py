from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .forms import ImageUploadForm
from .models import ImageUpload
import shutil
import random
import os
from django.conf import settings
from PIL import Image, ImageDraw, ImageEnhance

def white_black(image_url):
    image_url = image_url.lstrip('/')
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_path = image_path.replace('media/uploads/', 'uploads/')

    with Image.open(image_path) as img:
        blurred_img = img.convert('RGB')
        with Image.open(image_path) as img_1:
            blurred_img_1 = img_1.convert('RGB')

            for i in range(img.width):
                for j in range(img.height):
                    distance_to_center = ((i - img.width // 2) ** 2 + (j - img.height // 2) ** 2) ** 0.5
                    intensity = int(255 * (distance_to_center / max(img.width, img.height)))
                    r, g, b = blurred_img.getpixel((i, j))
                    new_r = max(0, r + intensity // 2)
                    new_g = max(0, g + intensity // 2)
                    new_b = max(0, b + intensity // 2)
                    new_r_1 = max(0, r - intensity // 2)
                    new_g_1 = max(0, g - intensity // 2)
                    new_b_1 = max(0, b - intensity // 2)
                    blurred_img.putpixel((i, j), (new_r, new_g, new_b))
                    blurred_img_1.putpixel((i, j), (new_r_1, new_g_1, new_b_1))

            blurred_image_path = os.path.splitext(image_path)[0] + '_white.jpg'
            blurred_img.save(blurred_image_path, 'JPEG')
            blurred_image_path_1 = os.path.splitext(image_path)[0] + '_black.jpg'
            blurred_img_1.save(blurred_image_path_1, 'JPEG')

            blurred_image_url = os.path.join(settings.MEDIA_URL_1, os.path.basename(blurred_image_path))
            blurred_image_url_1 = os.path.join(settings.MEDIA_URL_1, os.path.basename(blurred_image_path_1))
            return blurred_image_url, blurred_image_url_1

def crack_white_black(image_url, value=60):
    image_url = image_url.lstrip('/')
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_path = image_path.replace('media/uploads/', 'uploads/')

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        draw = ImageDraw.Draw(img)
        with Image.open(image_path) as img_1:
            img_1 = img_1.convert('RGB')
            draw_1 = ImageDraw.Draw(img_1)

            for _ in range(value):
                start_x = random.randint(0, img.width - 80)
                start_y = random.randint(0, img.height - 80)
                end_x = random.randint(start_x, min(start_x + 80, img.width))
                end_y = random.randint(start_y, min(start_y + 80, img.height))

                draw.line([(start_x, start_y), (end_x, end_y)], fill=(255, 255, 255), width=1)
                draw_1.line([(start_x, start_y), (end_x, end_y)], fill=(0, 0, 0), width=1)

            blurred_img = img
            blurred_img_1 = img_1

            blurred_image_path = os.path.splitext(image_path)[0] + '_blurred_white.jpg'
            blurred_img.save(blurred_image_path, 'JPEG')
            blurred_image_path_1 = os.path.splitext(image_path)[0] + '_blurred_black.jpg'
            blurred_img_1.save(blurred_image_path_1, 'JPEG')

            blurred_image_url = os.path.join(settings.MEDIA_URL_1, os.path.basename(blurred_image_path))
            blurred_image_url_1 = os.path.join(settings.MEDIA_URL_1, os.path.basename(blurred_image_path_1))
            return blurred_image_url, blurred_image_url_1


def new_black_white(image_url, value=300):
    image_url = image_url.lstrip('/')
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_path = image_path.replace('media/uploads/', 'uploads/')

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        draw = ImageDraw.Draw(img)
        with Image.open(image_path) as img_1:
            img_1 = img_1.convert('RGB')
            draw_1 = ImageDraw.Draw(img_1)

            for _ in range(value):
                x = random.randint(0, img.width - 3)
                y = random.randint(0, img.height - 3)
                g, k = random.randint(0, 30), random.randint(0, 10)
                for i in range(g):
                    for j in range(k):
                        draw.point((x + i, y + j), fill=(0, 0, 0))
                        draw_1.point((x + i, y + j), fill=(255, 255, 255))

            blurred_img = img.convert('RGB')
            blurred_img_1 = img_1.convert('RGB')

            blurred_image_path = os.path.splitext(image_path)[0] + '_new_black.jpg'
            blurred_img.save(blurred_image_path, 'JPEG')
            blurred_image_path_1 = os.path.splitext(image_path)[0] + '_new_white.jpg'
            blurred_img_1.save(blurred_image_path_1, 'JPEG')

            blurred_image_url = os.path.join(settings.MEDIA_URL_1, os.path.basename(blurred_image_path))
            blurred_image_url_1 = os.path.join(settings.MEDIA_URL_1, os.path.basename(blurred_image_path_1))
            return blurred_image_url, blurred_image_url_1

def change_noise(image_url, noise):
    image_url = image_url.lstrip('/')
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_path = image_path.replace('media/uploads/', 'uploads/')

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(noise / 100.0)

        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(noise / 100.0)

        img = img.convert('RGB')

        image_path = os.path.splitext(image_path)[0] + '_noise.jpg'
        img.save(image_path, 'JPEG')
        image_url = os.path.join(settings.MEDIA_URL_1, os.path.basename(image_path))
        return image_url


def add_sepia(image_url, sepia_value):
    image_url = image_url.lstrip('/')
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_path = image_path.replace('media/uploads/', 'uploads/')

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        sepia_img = img.copy()
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = sepia_img.getpixel((i, j))
                r = int((0.393 * r + 0.769 * g + 0.189 * b) * sepia_value / 100) + 70
                g = int((0.349 * r + 0.686 * g + 0.168 * b) * sepia_value / 100) + 70
                b = int((0.272 * r + 0.534 * g + 0.131 * b) * sepia_value / 100) + 70
                r = min(max(r, 0), 255)
                g = min(max(g, 0), 255)
                b = min(max(b, 0), 255)
                sepia_img.putpixel((i, j), (r, g, b))
        sepia_img= sepia_img.convert('RGB')

        image_path = os.path.splitext(image_path)[0] + '_sepia.jpg'
        sepia_img.save(image_path, 'JPEG')
        image_url = os.path.join(settings.MEDIA_URL_1, os.path.basename(image_path))
        return image_url

def add_yell(image_url, glitch_value):
    image_url = image_url.lstrip('/')
    image_path = os.path.join(settings.MEDIA_ROOT, image_url)
    image_path = image_path.replace('media/uploads/', 'uploads/')

    with Image.open(image_path) as img:
        img = img.convert('RGB')
        sepia_img = img.copy()

        for i in range(img.width):
            for j in range(img.height):
                r, g, b = sepia_img.getpixel((i, j))
                r = int((r + (r * 0.3) - (g * 0.2) - (b * 0.1)) * glitch_value / 100) + 100
                g = int((g - (r * 0.1) + (g * 0.2) - (b * 0.3)) * glitch_value / 100) + 100
                b = int(((r * 0.2) - (g * 0.3) + (b * 0.1)) * glitch_value / 100) + 100
                r = min(max(r, 0), 255)
                g = min(max(g, 0), 255)
                b = min(max(b, 0), 255)
                sepia_img.putpixel((i, j), (r, g, b))

        sepia_img = sepia_img.convert('RGB')
        image_path = os.path.splitext(image_path)[0] + '_glitch.jpg'
        sepia_img.save(image_path, 'JPEG')
        image_url = os.path.join(settings.MEDIA_URL_1, os.path.basename(image_path))
        return image_url



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = request.FILES['image'].name
            if not file_name.lower().endswith(('.jpg', '.jpeg')):
                return render(request, 'editor/upload.html',
                              {'form': form, 'error': 'Загрузите файл с расширением .jpg или .jpeg'})

            form.save()
            hotels = ImageUpload.objects.last()
            data = {
                'image_url': hotels.image.url,
                'sepia': "",
                'glitch': "",
            }
            data['my_image_url'] = data['image_url']
            data['crack_white'], data['crack_black'] = crack_white_black(data['image_url'])
            data['new_black'], data['new_white'] = new_black_white(data['image_url'])
            data['white'], data['black'] = white_black(data['image_url'])

            query_string = urlencode(data)
            return redirect(f"{reverse('change_image')}?{query_string}")
    else:
        form = ImageUploadForm()

    return render(request, 'editor/upload.html', {'form': form})

def change_image(request):
    data = request.GET.dict()

    if request.method == 'POST':
        flag = 0
        if 'download' in request.POST or 'cancel' in request.POST:
            image_path = os.path.join(settings.MEDIA_ROOT)

            try:
                shutil.rmtree(image_path)
                print(f"Folder {image_path} cleaned successfully")
            except FileNotFoundError:
                print(f"Folder {image_path} not found")
            except Exception as e:
                print(f"Error cleaning folder {image_path}: {e}")

            return redirect('upload_image')
        elif 'value_new' in request.POST:
            flag = 1
            p = int(request.POST.get('new'))
            data['new_black'], data['new_white'] = new_black_white(data['my_image_url'], value=p)
        elif 'value_crack' in request.POST:
            flag = 1
            p = int(request.POST.get('crack'))
            data['crack_white'], data['crack_black'] = crack_white_black(data['my_image_url'], value=p)
        elif 'glitch' in request.POST:
            data['my_image_url'] = data['glitch']
        elif "sepia" in request.POST:
            data['my_image_url'] = data['sepia']
        elif "noise" in request.POST:
            p = int(request.POST.get("noise_value"))
            data['my_image_url'] = change_noise(data['my_image_url'], p)
        elif 'look_g' in request.POST:
            p = int(request.POST.get("glitch_value"))
            data['glitch'] = add_yell(data['my_image_url'], p)
        elif 'look_s' in request.POST:
            p = int(request.POST.get("sepia_value"))
            data['sepia'] = add_sepia(data['my_image_url'], p)
        elif 'white' in request.POST:
            data['my_image_url'] = data['white']
        elif 'black' in request.POST:
            data['my_image_url'] = data['black']
        elif 'original' in request.POST:
            data['my_image_url'] = data['image_url']
        elif 'crack_white' in request.POST:
            data['my_image_url'] = data['crack_white']
        elif 'crack_black' in request.POST:
            data['my_image_url'] = data['crack_black']
        elif 'new_white' in request.POST:
            data['my_image_url'] = data['new_white']
        elif 'new_black' in request.POST:
            data['my_image_url'] = data['new_black']
        if flag == 0:
            data['crack_white'], data['crack_black'] = crack_white_black(data['my_image_url'])
            data['new_black'], data['new_white'] = new_black_white(data['my_image_url'])
            data['white'], data['black'] = white_black(data['my_image_url'])

        query_string = urlencode(data)
        return redirect(f"{reverse('change_image')}?{query_string}")

    return render(request, 'editor/result.html', {'data': data})