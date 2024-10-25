import pypdf
PDF_FILENAME = 'Recursion_Chapter1.pdf'

reader = pypdf.PdfReader(PDF_FILENAME)
image_num = 0
for i, page in enumerate(reader.pages):
    print(f'Reading page {i+1} - {len(page.images)} images found...')
    try:
        for image in page.images:
            with open(f'{image_num}_page{i+1}_{image.name}', 'wb') as file:
                file.write(image.data)
            print(f'Wrote {image_num}_page{i+1}_{image.name}...')
            image_num += 1
    except Exception as exc:
        print(f'Skipped page {i+1} due to error: {exc}')
