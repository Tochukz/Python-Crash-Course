position="Cloud architect"
job_position="Solution architect"
print(position.title())
print(position.upper())

name="Tochukwu"
# Working with f-string 
who_am_i=f"{name} is a {position.title()}"
print(who_am_i)

#using format()
who_am_i="{} is a {}".format(name, job_position.title())
print(who_am_i)

first="Java "
second=" Script "
print(f"{first}{second}")
print(f"{first.rstrip()}{second}")
print(f"{first.rstrip()}{second.lstrip()}")
print(f"Coffee{second.strip()}3")