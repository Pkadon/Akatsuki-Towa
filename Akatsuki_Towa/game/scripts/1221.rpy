label avg1221:

play music "ED6101.ogg"
scene avg_bg_064
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(2110149)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110150)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110151)]'
stop music
scene avg_bg_011
$ update_narrator('c191')
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
with fade
$ update_portrait('sc011_01 4', 'p19', [l(-1), l_shake, light, flip], 6)
c191 '[convertstrid(2110152)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110153)]'
play music "ed7513.ogg"
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110154)]'
hide p19
$ update_portrait('sc012_01 4', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110155)]'
hide p21
c27001 '[convertstrid(2110156)]' with shake
hide p20
$ update_portrait('sc013_01 3', 'p21', [r(-12), light], 5)
c213 '[convertstrid(2110157)]'
scene avg_bg_064
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
with fade
c13 '[convertstrid(2110158)]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110159)]'
scene avg_bg_011
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
with fade
c201 '[convertstrid(2110160)]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
c201 '[convertstrid(2110161)]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 6)
$ update_portrait('sc011_01 4', 'p19', [r(-1), light], 5)
c193 '[convertstrid(2110162)]'
$ update_portrait('sc011_01 4', 'p19', [r(-1), light], 5)
c193 '[convertstrid(2110163)]'
$ update_portrait('sc011_01 4', 'p19', [r(-1), light], 5)
c193 '[convertstrid(2110164)]'
$ update_portrait('sc011_01 4', 'p19', [r(-1), dark], 5)
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
c201 '[convertstrid(2110165)]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
c201 '[convertstrid(2110166)]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 6)
$ update_portrait('sc011_01 4', 'p19', [r(-1), light], 5)
c193 '[convertstrid(2110167)]'
hide p20
$ update_portrait('sc011_01 4', 'p19', [r(-1), dark], 5)
$ update_portrait('sc013_01 2', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110168)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110169)]'
hide p21
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
c201 '[convertstrid(2110170)]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 6)
$ update_portrait('sc011_01 4', 'p19', [r(-1), light], 5)
c193 '[convertstrid(2110171)]'
hide p20
$ update_portrait('sc011_01 4', 'p19', [r(-1), dark], 5)
$ update_portrait('sc013_01 2', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110172)]'
hide p19
$ update_portrait('sc013_01 2', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110173)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 3', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110174)]'
scene avg_bg_064
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
with fade
c13 '[convertstrid(2110175)]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110176)]'
scene avg_bg_011
$ update_portrait('sc011_01 3', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
with fade
c191 '[convertstrid(2110177)]' with shake
scene avg_bg_064
$ update_narrator('c191')
$ update_portrait('sc011_01 3', 'p19', [l(-1), light, flip], 6)
with fade
$ update_portrait('sc011_01 3', 'p19', [l_exit(-1), light, flip], 6)
play sfx2 "other_7045.ogg"
c191 '[convertstrid(2110178)]'
hide p19
stop music
$ update_portrait('oc001_01 12', 'p1', [r_entrance(-2), r_shake, light], 5)
c13 '[convertstrid(2110179)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110180)]'
play music "ed7513.ogg"
scene avg_bg_011
$ update_narrator('c211')
with fade
$ update_portrait('sc013_01 4', 'p21', [l_entrance(-12), light, flip], 6)
c211 '[convertstrid(2110181)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110182)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110183)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110184)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110185)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110186)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110187)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110188)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110189)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110190)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110191)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110192)]'
$ update_portrait('sc012_01 4', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110193)]'
hide p21
$ update_portrait('sc012_01 4', 'p20', [r(-16), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(2110194)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc012_01 2', 'p20', [r(-16), r_shake, light], 5)
c203 '[convertstrid(2110195)]'
hide p1
$ update_portrait('sc012_01 2', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110196)]'
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110197)]'
$ update_portrait('sc013_01 1', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('sc012_01 3', 'p20', [r(-16), light], 5)
c203 '[convertstrid(2110198)]'
$ update_portrait('sc012_01 3', 'p20', [r(-16), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110199)]'
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110200)]'
hide p20
$ update_portrait('sc013_01 1', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110201)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110202)]'
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(2110203)]'
$ update_portrait('sc013_01 1', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110204)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110205)]'
stop music
scene avg_bg_064
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(2110206)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(2110207)]'
hide p1
$ update_narrator('c13')
with fade
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 5)
play sfx2 "other_7085.ogg"
c13 '[convertstrid(2110208)]'
$ update_portrait('oc001_01 10', 'p1', [r_midback(-2), light], 5)
c13 '[convertstrid(2110209)]'
play music "ed7515.ogg"
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110210)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110211)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 3', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110212)]'
$ update_portrait('sc011_01 3', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110213)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110214)]'
$ update_portrait('sc011_01 2', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110215)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110216)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110217)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110218)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110219)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110220)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110221)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110222)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110223)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110224)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110225)]'
$ update_portrait('sc011_01 3', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110226)]'
$ update_portrait('sc011_01 3', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110227)]'
$ update_portrait('sc011_01 3', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110228)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), l_shake, light, flip], 6)
c191 '[convertstrid(2110229)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110230)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110231)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110232)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110233)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110234)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110235)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110236)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110237)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110238)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110239)]'
play music "ed7565.ogg"
$ update_portrait('sc011_01 1', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110240)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110241)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110242)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110243)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110244)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110245)]'
$ update_portrait('sc011_01 1', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110246)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 3', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(2110247)]'
$ update_portrait('sc011_01 5', 'p19', [l(-1), l_shake, light, flip], 6)
c191 '[convertstrid(2110248)]'
$ update_portrait('sc011_01 5', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(2110249)]'
return