label avg25096:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 5)
$ update_narrator('c5873')
window show
with fade_in
c5873 '[textdict[1210269]]'
$ update_portrait('uc001_01 2', 'p587', [mid(-2), light], 5)
c5873 '[textdict[1210270]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25097
    "[textdict[1215000]]":
        call avg25026
return