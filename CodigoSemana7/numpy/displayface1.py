import imageio

face = imageio.imread('face.png')
print(face)

print(type(face) )    
print(face.shape )
print(face.dtype )