#coding:utf-8

# P139，证明书中写错了......
sourceDict = {"name0": "0", "name1": "1", "name2": "2"}
targetDict = sourceDict.copy()
print "修改前，目标字典为:", targetDict
print "修改目标字典"
targetDict["name0"] = "target_0"
print "修改后，目标字典为:", targetDict
print "修改后，原字典为:", sourceDict
print "修改原字典"
sourceDict["name0"] = "source_0"
print "修改后，目标字典为:", targetDict
print "修改后，原字典为:", sourceDict

