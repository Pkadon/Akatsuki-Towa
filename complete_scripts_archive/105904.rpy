label avg105904:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 3', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with fade_in
c591 '[convertstrid(1219257)]'
$ update_portrait('sc052_01 3', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(1219258)]'
$ update_portrait('sc052_01 3', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1219259)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(1219260)]'
menu:
    extend ""
    "[textdict[1219261]]":
        call avg105905
    "[textdict[1219262]]":
        call avg105906
    "[textdict[1219263]]":
        call avg105907
return