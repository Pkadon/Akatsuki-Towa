label avg101104:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1220399]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc003_01 6', 'p11', [l(-4), light, flip], 6)
c111 '[textdict[1220400]]'
$ update_portrait('sc003_01 6', 'p11', [l(-4), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1220401]]'
menu:
    extend ""
    "[textdict[1220402]]":
        call avg101105
    "[textdict[1220403]]":
        call avg101106
    "[textdict[1220404]]":
        call avg101107
return