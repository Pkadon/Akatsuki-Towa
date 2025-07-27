label avg25054:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 2', 'p2006', [mid(6), light], 5)
$ update_narrator('c20063')
window show
with fade_in
c20063 '[convertstrid(1210149)]'
hide p2006
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[convertstrid(1210150)]'
hide p2
$ update_portrait('uc001_02 2', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210151)]'
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210152)]'
hide p2006
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1210153)]'
hide p2
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210154)]'
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210155)]'
return