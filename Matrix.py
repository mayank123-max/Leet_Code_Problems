Mat = [[1,2,3],[4,5,6],[7,8,9]]
print("Original Matrix:-")
for i in Mat:
    print(i)
# Mat = list(map(list,zip(*Mat)))
# print("Transposed Matrix:-")
# for i in Mat:
#     print(i)
# print("Rotated Right 90 degrees:-")
# for i in range(len(Mat)):
#     Mat[i] = Mat[i][::-1]
# print(Mat)
N = len(Mat)
for i in range(N):
    for j in range(i+1, N):
        Mat[i][j] , Mat[j][i] = Mat[j][i] , Mat[i][j]
print("Transposed Matrix:-")
for i in Mat:
    print(i)