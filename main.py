import text_to_speech
import img_to_text

image = 'Write-a-Paragraph-Step-10-Version-4.jpg'

text = img_to_text.change_to_text(image)
temp = text_to_speech.change_to_speech(text)

text_to_speech.play_the_speech()