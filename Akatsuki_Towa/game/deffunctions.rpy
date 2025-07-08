init python:
    def update_portrait(portrait, alias, atlist, z):
        if renpy.showing(alias):
            renpy.hide(alias)
        renpy.show(portrait, at_list=atlist, tag=alias, zorder=z)