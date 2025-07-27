label avg100908:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1218033)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[convertstrid(1218034)]'
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1218035)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
c91 '[convertstrid(1218036)]'
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
c91 '[convertstrid(1218037)]'
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1218038)]'
menu:
    extend ""
    "[textdict[1218039]]":
        call avg100909
    "[textdict[1218040]]":
        call avg100910
    "[textdict[1218041]]":
        call avg100911
return