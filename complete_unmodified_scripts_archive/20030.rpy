label avg20030(trans=fade_in):

$ play_music("ed7150.ogg")
scene placeholderbackground
$ update_portrait('oc004_01 1', 'p4', [mid(-5), light], 6)
$ update_narrator('c43')
window show
with trans
play sfxvoice "avg_vocal_li06.ogg"
get_char('c43') '[convertstrid(1002138)]' (**arg(1, 1002138))
return "avg20030"