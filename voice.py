from text_to_speech import save

text = '''
Watch your tongue or have it cut from your head
Save your life by keeping whispers unsaid
Children roam the streets, now orphans of war
Bodies hanging in the streets to adore
pre-chorus
Royal flames will carve a path in chaos
Bringing daylight to the night
Death is riding into town with armor
They′ve come to take all your rights

Hail to the king
Hail to the one
Kneel to the crown
Stand in the sun
Hail to the king
(Hail, hail, hail!)
The king

Blood is spilt while holding keys to the throne
Born again, but it's too late to atone
No mercy from the edge of the blade
Dare escape and learn the price to be paid
pre-chorus
Let the water flow with shades of red now
Arrows black out all the light (light)
Death is riding into town with armor
They′ve come to grant you your rights

Hail to the king
Hail to the one
Kneel to the crown
Stand in the sun
Hail to the king
(Hail, hail, hail!)
The king
bridge
There's a taste of fear
When the henchmen call
Iron fist to tame the land
Iron fist to claim it all
chorus
Hail to the king
Hail to the one
Kneel to the crown'''
language = "en"  # Specify the language (IETF language tag)
output_file = '''verse
Watch your tongue or have it cut from your head
Save your life by keeping whispers unsaid
Children roam the streets, now orphans of war
Bodies hanging in the streets to adore
pre-chorus
Royal flames will carve a path in chaos
Bringing daylight to the night
Death is riding into town with armor
They′ve come to take all your rights
chorus
Hail to the king
Hail to the one
Kneel to the crown
Stand in the sun
Hail to the king
(Hail, hail, hail!)
The king
verse
Blood is spilt while holding keys to the throne
Born again, but it's too late to atone
No mercy from the edge of the blade
Dare escape and learn the price to be paid
pre-chorus
Let the water flow with shades of red now
Arrows black out all the light (light)
Death is riding into town with armor
They′ve come to grant you your rights
chorus
Hail to the king
Hail to the one
Kneel to the crown
Stand in the sun
Hail to the king
(Hail, hail, hail!)
The king
bridge
There's a taste of fear
When the henchmen call
Iron fist to tame the land
Iron fist to claim it all
chorus
Hail to the king
Hail to the one
Kneel to the crown'''  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)