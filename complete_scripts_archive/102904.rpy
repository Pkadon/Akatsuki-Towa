label avg102904:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1219907)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1219908)]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1219909)]'
menu:
    extend ""
    "[textdict[1219910]]":
        call avg102905
    "[textdict[1219911]]":
        call avg102906
    "[textdict[1219912]]":
        call avg102907
return