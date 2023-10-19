#No se puede llamar al fichero o al archivo wikipedia
import wikipedia
wikipedia.set_lang('es')
resultado = wikipedia.summary("absolute zero", sentences = 2)

print(resultado)
español = wikipedia.languages()
