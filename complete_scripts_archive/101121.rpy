label avg101121:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1220446)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc003_01 2', 'p11', [l(-4), light, flip], 6)
c111 '[convertstrid(1220447)]'
$ update_portrait('sc003_01 2', 'p11', [l(-4), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1220448)]'
menu:
    extend ""
    "[textdict[1220449]]":
        call avg101122
    "[textdict[1220450]]":
        call avg101123
    "[textdict[1220451]]":
        call avg101124
return