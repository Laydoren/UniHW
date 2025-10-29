isRoles = False

roles = {}
num_line = 0
curr_role = ""
role_lines = []

with open("roles.txt", "r", encoding="utf8") as file:
    for line in file:

        if line == "textLines:\n":
            isRoles = False
            role_lines.clear()
            continue

        if isRoles == True:
            roles[line.strip("\n") + ":"] = []

        if isRoles == False:
            if ":" in line:

                for role in roles.keys():
                    if " " + role not in line and role in line:
                        if curr_role != "": roles[curr_role].append(role_lines)
                        num_line += 1
                        line = line.replace(role,str(num_line)+")")
                        curr_role = role
                        role_lines = []
                        break

            role_lines.append(line)

        if line == "roles:\n":
            isRoles = True
            role_lines.clear()
            continue

roles = dict(sorted(roles.items(), key=lambda x: (len(x[1]) == 0, x[0])))
file.close()

res_text = open("res.txt", "w", encoding="utf-8")
for role, phrase in roles.items():
    res_text.write(role+"\n")
    for line in phrase:
        for x in line: res_text.write(x)
    res_text.write("\n")
res_text.close()