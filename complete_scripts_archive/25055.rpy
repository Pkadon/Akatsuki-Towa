label avg25055:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
$ update_narrator('c20063')
window show
with fade_in
c20063 '[convertstrid(1210156)]'
$ update_portrait('uc001_02 2', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210157)]'
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210158)]'
hide p2006
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210159)]'
hide p1
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
c20063 '[convertstrid(1210160)]'
hide p2006
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na17.ogg"
c13 '[convertstrid(1210161)]'
hide p1
$ update_portrait('uc001_02 1', 'p2006', [mid(6), light], 5)
play sfx2 "common_35rewardholy.ogg"
c20063 '[convertstrid(1210162)]'
return