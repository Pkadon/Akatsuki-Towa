label avg101808:

stop music
scene placeholderbackground
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
$ update_narrator('c181')
window show
with fade_in
c181 '[convertstrid(1222176)]'
$ update_portrait('sc010_01 1', 'p18', [l(-10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1222177)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
c181 '[convertstrid(1222178)]'
menu:
    extend ""
    "[textdict[1222179]]":
        call avg101809
    "[textdict[1222180]]":
        call avg101810
    "[textdict[1222181]]":
        call avg101811
return