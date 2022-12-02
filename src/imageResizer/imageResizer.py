import os
import cv2
import argparse

# Defining terminal arguments, both are optional and have default values
parser = argparse.ArgumentParser()
parser.add_argument('--inputFolder', type=str, help="Input folder of images you want to resize", default="../Training/smash")
parser.add_argument('--outputFolder', type=str, help="Output folder for saveing resized images", default="../../data/resizedImages")
args = parser.parse_args()

# Amount of completed resized images (for printing progress)
currentIndex = 0

inputDir = args.inputFolder


# Create a new output directory if it doesn't exist
if not os.path.exists(args.outputFolder):
   os.makedirs(args.outputFolder)
   print(f"Created output directory at {args.outputFolder}")

# os.listdir(inputDir) returns a list of items inside a folder
totalImageCount = len(os.listdir(inputDir))
for imagePath in os.listdir(inputDir):

    # Splits a file path into path and extension
    fileDetails = os.path.splitext(f'{inputDir}/{imagePath}')

    # Not interested in the full path, only the file name
    fileName = fileDetails[0].rsplit("/",1)[1]
    fileExtension = fileDetails[1]

    # Load image
    img = cv2.imread(f'{inputDir}/{imagePath}', cv2.IMREAD_UNCHANGED)
 
    # Resize image to a 32x32 square
    resized = cv2.resize(img, (32, 32), interpolation = cv2.INTER_AREA)

    # Save image in the data
    cv2.imwrite(f"{args.outputFolder}/{fileName}_32x32{fileExtension}", resized)

    currentIndex += 1
    print(f"Resized {imagePath} from {img.shape} to {resized.shape}! {currentIndex}/{totalImageCount} completed...")

    if currentIndex >= totalImageCount:
        print(f"Finished resizing {totalImageCount} images!")