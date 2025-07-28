label avg105204:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 3', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with fade_in
c591 '[convertstrid(1219257)]'
$ update_portrait('sc052_01 3', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(1219258)]'
$ update_portrait('sc052_01 3', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1219259)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(1219260)]'
menu:
    extend ""
    "[textdict[1219261]]":
        call avg105205
    "[textdict[1219262]]":
        call avg105206
    "[textdict[1219263]]":
        call avg105207
return