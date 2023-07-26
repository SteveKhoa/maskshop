# Masking Workshop (maskshop)

Generate mask image for image processing tasks in Python.

For now, the primary scope of this package is to provide quick masks to deal with 2D shifted Fourier-transformed images. The package provides simple masks such as square, circle, vertical & horizontal line and smooth transitioning instances of the above shapes (which is widely used to mitigate Fourier ringing effects). By using this package, programmers do not need to code every mask from scratch each time filtering is performed.

In the future, the package expects to extract more complicated, high-level computer vision shapes from automated 
segmentation such as face segmentation or background removal, as well as other masks on spatial domains.

All contributions and suggestions are welcomed!