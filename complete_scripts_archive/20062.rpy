label avg20062:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1003003)]'
menu:
    extend ""
    "[textdict[1003004]]":
        call avg0
    "[textdict[1003005]]":
        call avg0
    "[textdict[1003006]]":
        call avg0
return