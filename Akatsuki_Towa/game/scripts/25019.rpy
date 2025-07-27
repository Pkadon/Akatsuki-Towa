label avg25019:

stop music
scene placeholderbackground
$ update_narrator('c20083')
window show
with fade_in
c20083 '[convertstrid(1210042)]'
c20093 '[convertstrid(1210043)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210044)]'
hide p2
c20083 '[convertstrid(1210045)]'
c20093 '[convertstrid(1210046)]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25020
    "[textdict[1215000]]":
        call avg25026
return