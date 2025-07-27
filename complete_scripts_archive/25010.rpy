label avg25010:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 5)
$ update_narrator('c5873')
window show
with fade_in
c5873 '[convertstrid(1210016)]'
hide p587
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210017)]'
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 5)
c5873 '[convertstrid(1210018)]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25011
    "[textdict[1215000]]":
        call avg25000
return