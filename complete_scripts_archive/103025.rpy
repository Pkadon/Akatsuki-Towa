label avg103025:

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
$ update_narrator('c301')
window show
with fade_in
c301 '[convertstrid(1222484)]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1222485)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1222486)]'
menu:
    extend ""
    "[textdict[1222487]]":
        call avg103026
    "[textdict[1222488]]":
        call avg103027
    "[textdict[1222489]]":
        call avg103028
return