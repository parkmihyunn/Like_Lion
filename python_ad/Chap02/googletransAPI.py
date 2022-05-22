from googletrans import Translator

translator = Translator()

translation = translator.translate("Hello. Nice to meet you.", dest='ko')
print(translation.origin)
print(translation.text + "\n")

sentence = input("번역을 원하는 문장을 입력하세요 : ")
result = translator.translate(sentence, dest="en")
detect = translator.detect(sentence)

print("\n============= 번역 결과 =============\n")
print(detect.lang,":", result.origin)
print(result.dest,":", result.text)
print("\n======================================\n")