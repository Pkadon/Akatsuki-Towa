label avg105225:

stop music
scene placeholderbackground
$ update_portrait('sc052_01 6', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with fade_in
c591 '[textdict[1219319]]'
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1219320]]'
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1219321]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1219322]]'
menu:
    extend ""
    "[textdict[1219323]]":
        call avg105226
    "[textdict[1219324]]":
        call avg105227
    "[textdict[1219325]]":
        call avg105228
return