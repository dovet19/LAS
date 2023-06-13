import lasio
import lasio.examples

# # Read LAS file using LASIO
# las = lasio.read("Data/382605076430201.20020311.ZH.las")

# las.section.keys()

# las.sections['Version']

las = lasio.examples.open("1001178659.las")

las.version