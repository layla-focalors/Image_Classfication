from transformers import pipeline
clf = pipeline(task='image-classification', model='google/vit-base-patch16-224')

clf('./cat1.webp')
clf.save('./vit')