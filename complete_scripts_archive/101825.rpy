label avg101825:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1222226)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
c181 '[convertstrid(1222227)]'
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
c181 '[convertstrid(1222228)]'
menu:
    extend ""
    "[textdict[1222229]]":
        call avg101826
    "[textdict[1222230]]":
        call avg101827
    "[textdict[1222231]]":
        call avg101828
return