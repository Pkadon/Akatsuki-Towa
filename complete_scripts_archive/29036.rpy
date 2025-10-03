label avg29036:

$ play_music("ED6104.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1100019)]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg29037
    "[textdict[1215000]]":
        call avg29025
return