import dictionary1

print(dictionary1.d)

text = " hello my name is  armando  "


translate = ""

words = text.split()

for w in words:

    translate = translate + " " + dictionary1.d[w]

print(translate)

