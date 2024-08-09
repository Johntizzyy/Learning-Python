def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print('Done with the function')
        return wrapper

# @announce
# def sayHello():
#     print("Hello world")
# sayHello()

person = [
    {'name':'Johntizzy',"initials":"AJB"},
    {'name':'Dave',"initials":"POG"},
    {'name':'Peace',"initials":"DPF"},
]

# def f(person):
#     return person['name']
person.sort(key =lambda person: person['name'])

print(person)

# Discussion about heighting system as related to geodetic survey

'''

Heighting systems in geodetic surveying are critical for accurately measuring vertical positions relative to a reference surface. These systems are essential for various applications, including mapping, construction, and scientific research. Below is a broad discussion of heighting systems, their classifications, measurement techniques, and challenges.

## Height Definitions

In geodetic surveying, several types of heights are defined, each with its own reference surface:

1. **Ellipsoidal Height (H)**: This is the height of a point above a mathematical ellipsoid, which approximates the shape of the Earth. It is primarily used in GPS measurements.

2. **Orthometric Height (h)**: This height measures the distance from a point on the Earth's surface to the geoid, which represents mean sea level. Orthometric heights are physically meaningful and widely used in engineering and construction.

3. **Normal Height (N)**: Similar to orthometric height, normal height is defined as the distance from a point to a quasi-geoid along the vertical line through that point. It is less common in practice but relevant in specific geodetic contexts.

### Relationship Between Heights

The relationship between these height types is crucial for conversions:

- **Orthometric Height** = **Ellipsoidal Height** - **Geoid Undulation** 

This formula highlights the necessity of accurate geoid models to convert ellipsoidal heights to orthometric heights effectively.

## Measurement Techniques

### GPS Heighting

Global Positioning System (GPS) technology has transformed height measurement by providing three-dimensional positioning capabilities. However, GPS primarily measures ellipsoidal heights, necessitating conversion to orthometric heights using geoid models. The limitations of GPS heighting include:

- **Geoid Modeling**: The accuracy of geoid models affects the conversion process, as variations in geoid undulation can significantly impact height measurements. For example, undulations can reach up to 200 meters in some regions, complicating accurate height determination[1][2].

- **Quality of Measurements**: The precision of GPS measurements can be influenced by factors such as satellite geometry, atmospheric conditions, and multipath effects. Techniques like Real-Time Kinematic (RTK) surveying are employed to enhance accuracy, but they require careful management of phase ambiguities and redundancy in measurements to mitigate errors[1].

### Traditional Heighting Methods

1. **Barometric Heighting**: This method utilizes the relationship between atmospheric pressure and height. While simple, it is less accurate and can yield uncertainties of about 10 meters, making it suitable for rough estimates rather than precise measurements.

2. **Trigonometric Heighting**: This technique involves measuring vertical angles between survey points and using trigonometry to calculate height differences. It can achieve decimeter-level accuracy over distances of up to 30 kilometers, provided that appropriate corrections for Earth's curvature and atmospheric refraction are applied[5].

3. **Optical Levelling**: Using an optical level, surveyors project a horizontal line to measure height differences. This method is reliable for determining heights with a few decimeters of uncertainty over moderate distances.

## Challenges in Heighting Systems

### Vertical Datum Issues

Different regions may use various vertical datums, complicating the integration of height measurements across areas. Height system unification efforts aim to standardize these datums, but discrepancies can still arise due to local variations and historical data differences[3].

### Earth’s Variability

The Earth's surface is not uniform; it changes due to tectonic activity, subsidence, and other geological processes. These changes must be accounted for in height systems, especially for long-term applications like 3D cadastres, which require stability over centuries[2].

### Accuracy and Precision

Achieving high accuracy in height measurements is challenging due to the inherent limitations of measurement techniques and the need for precise geoid models. The accuracy of height determination can vary significantly based on the method used and the scale of the survey[1][4].

## Conclusion

Heighting systems in geodetic surveying are complex and multifaceted, involving various height definitions, measurement techniques, and significant challenges in accuracy and consistency. Understanding the distinctions between ellipsoidal, orthometric, and normal heights, as well as the limitations of different measurement methods, is essential for effective geodetic practice and ensuring that height measurements are both meaningful and applicable to real-world scenarios.

Citations:
[1] https://www.fig.net/organisation/comm/5/library/reports/gavle/higgins.pdf
[2] https://www.fig.net/resources/proceedings/2011/2011_3dcadastre/3Dcad_2011_14.pdf
[3] https://www.researchgate.net/publication/278690726_Geodetic_World_Height_System_Unification
[4] https://digitalcommons.lib.uconn.edu/cgi/viewcontent.cgi?article=1001&context=nrme_articles
[5] https://www.icsm.gov.au/education/fundamentals-mapping/surveying-mapping/surveying-heights

'''