#Rotation from blender to FG in pyhton
#====================
#Use precise align to get the rotations in XYZ

    eul = mathutils.Euler((math.radians(68), math.radians(8), math.radians(5)), 'XYZ')
    quat = eul.to_quaternion()
    rot = quat.to_euler('YXZ')
    print('yxz')
    print(degrees(rot.x))
    print(degrees(rot.y))
    print(degrees(rot.z))