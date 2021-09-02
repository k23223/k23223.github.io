from glob import glob

file_list = glob('_posts/*.md')
for file in file_list:
    with open(file, 'r', encoding='utf8') as fp:
        md_text = fp.read()
        new_text = md_text.replace('.png-xpctf', '.png')
        new_file = file.replace('_posts', '_posts_bak')
        with open(new_file, 'w', encoding='utf8') as f1:
            f1.write(new_text)
            print(new_file)