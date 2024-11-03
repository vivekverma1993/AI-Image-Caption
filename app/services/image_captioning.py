from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image

def generate_caption(image_path):
    processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
    model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')

    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors='pt')

    with torch.no_grad():
        outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
