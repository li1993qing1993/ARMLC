from PIL import Image
from PIL import ImageFilter
import os


def transform_image(data_dir):
    print('transforming images')
    # get image filenames
    labelnames = os.listdir(data_dir)
    label_count = 1
    for label in labelnames:
        print("generate images for label %d" % label_count)
        label_count += 1
        label_dir = os.path.join(data_dir, label)
        filenames = os.listdir(label_dir)
        for f in filenames:
            count_f = len(filenames)
            f_path = os.path.join(label_dir, f)
            f_prefix_idx = f_path.rfind('.')
            im = Image.open(f_path)
            im_size = im.size
            wh_ratio = float(im_size[0]) / im_size[1]
            if im_size[1] > 500:
                im_tmp = im.resize((int(wh_ratio * 500), 500))
                im_blur = im_tmp.filter(ImageFilter.BLUR)
                #im_blur = im_blur.resize((im_size[0], im_size[1]))
                im_blur.save(f_path[:f_prefix_idx] + '_blur.jpg')
                im_sharpen = im_tmp.filter(ImageFilter.SHARPEN)
                #im_sharpen = im_sharpen.resize((im_size[0], im_size[1]))
                im_sharpen.save(f_path[:f_prefix_idx] + '_sharpen.jpg')
                im_smooth = im_tmp.filter(ImageFilter.SMOOTH)
                #im_smooth = im_smooth.resize((im_size[0], im_size[1]))
                im_smooth.save(f_path[:f_prefix_idx] + '_smooth.jpg')
                if count_f > 4:
                    continue
                im_unsharp = im_tmp.filter(ImageFilter.UnsharpMask)
                #im_unsharp = im_unsharp.resize((im_size[0], im_size[1]))
                im_unsharp.save(f_path[:f_prefix_idx] + '_unsharp.jpg')
                if count_f > 3:
                    continue
                im_detail = im_tmp.filter(ImageFilter.DETAIL)
                #im_detail = im_detail.resize((im_size[0], im_size[1]))
                im_detail.save(f_path[:f_prefix_idx] + '_detail.jpg')
                if count_f > 2:
                    continue
                im_gaussian = im_tmp.filter(ImageFilter.GaussianBlur)
                #im_gaussian = im_gaussian.resize((im_size[0], im_size[1]))
                im_gaussian.save(f_path[:f_prefix_idx] + '_gaussian.jpg')
            else:
                im_tmp = im
                im_blur = im_tmp.filter(ImageFilter.BLUR)
                im_blur.save(f_path[:f_prefix_idx] + '_blur.jpg')
                im_sharpen = im_tmp.filter(ImageFilter.SHARPEN)
                im_sharpen.save(f_path[:f_prefix_idx] + '_sharpen.jpg')
                im_smooth = im_tmp.filter(ImageFilter.SMOOTH)
                im_smooth.save(f_path[:f_prefix_idx] + '_smooth.jpg')
                if count_f > 4:
                    continue
                im_unsharp = im_tmp.filter(ImageFilter.UnsharpMask)
                im_unsharp.save(f_path[:f_prefix_idx] + '_unsharp.jpg')
                if count_f > 3:
                    continue
                im_detail = im_tmp.filter(ImageFilter.DETAIL)
                im_detail.save(f_path[:f_prefix_idx] + '_detail.jpg')
                if count_f > 2:
                    continue
                im_gaussian = im_tmp.filter(ImageFilter.GaussianBlur)
                im_gaussian.save(f_path[:f_prefix_idx] + '_gaussian.jpg')

    label_count = 1
    for label in labelnames:
        print("generate images for label %d" % label_count)
        label_count += 1
        label_dir = os.path.join(data_dir, label)
        filenames = os.listdir(label_dir)
        for f in filenames:
            count_f = len(filenames)
            f_path = os.path.join(label_dir, f)
            f_prefix_idx = f_path.rfind('.')
            im = Image.open(f_path)
            im_r90 = im.transpose(Image.ROTATE_90)
            im_r90.save(f_path[:f_prefix_idx] + '_r90.jpg')
            if count_f > 34:
                continue
            im_r180 = im.transpose(Image.ROTATE_180)
            im_r180.save(f_path[:f_prefix_idx] + '_r180.jpg')
            if count_f > 22:
                continue
            im_r270 = im.transpose(Image.ROTATE_270)
            im_r270.save(f_path[:f_prefix_idx] + '_r270.jpg')

    for label in labelnames:
        label_dir = os.path.join(data_dir, label)
        filenames = os.listdir(label_dir)
        if len(filenames) < 50:
            print('Label %s does not have enough images. It only has %d images' %(label, len(filenames)))
