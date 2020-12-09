
class Mscx:

    beginning = """<?xml version="1.0" encoding="UTF-8"?>
<museScore version="3.01">
  <programVersion>3.5.2</programVersion>
  <programRevision>465e7b6</programRevision>
  <Score>
    <LayerTag id="0" tag="default"></LayerTag>
    <currentLayer>0</currentLayer>
    <Division>480</Division>
    <Style>
      <pageWidth>8.27</pageWidth>
      <pageHeight>11.69</pageHeight>
      <pagePrintableWidth>7.4826</pagePrintableWidth>
      <Spatium>1.76389</Spatium>
      </Style>
    <showInvisible>1</showInvisible>
    <showUnprintable>1</showUnprintable>
    <showFrames>1</showFrames>
    <showMargins>0</showMargins>
"""

    meta_tags = """    <metaTag name="arranger">{}</metaTag>
    <metaTag name="composer">{}</metaTag>
    <metaTag name="copyright">{}</metaTag>
    <metaTag name="creationDate">{}</metaTag>
    <metaTag name="lyricist">{}</metaTag>
    <metaTag name="movementNumber">{}</metaTag>
    <metaTag name="movementTitle">{}</metaTag>
    <metaTag name="platform">{}</metaTag>
    <metaTag name="poet">{}</metaTag>
    <metaTag name="source">{}</metaTag>
    <metaTag name="translator">{}</metaTag>
    <metaTag name="workNumber">{}</metaTag>
    <metaTag name="workTitle">{}</metaTag>
"""

    four_piano_parts = """    <Part>
      <Staff id="1">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        <bracket type="0" span="4" col="0"/>
        </Staff>
      <trackName>Soprano</trackName>
      <Instrument>
        <longName>Soprano</longName>
        <shortName>S.</shortName>
        <trackName>Soprano</trackName>
        <minPitchP>60</minPitchP>
        <maxPitchP>84</maxPitchP>
        <minPitchA>60</minPitchA>
        <maxPitchA>79</maxPitchA>
        <instrumentId>voice.soprano</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="0"/>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="2">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Alto</trackName>
      <Instrument>
        <longName>Alto</longName>
        <shortName>A.</shortName>
        <trackName>Alto</trackName>
        <minPitchP>52</minPitchP>
        <maxPitchP>77</maxPitchP>
        <minPitchA>55</minPitchA>
        <maxPitchA>74</maxPitchA>
        <instrumentId>voice.alto</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="0"/>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="3">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        <defaultClef>G8vb</defaultClef>
        </Staff>
      <trackName>Tenor</trackName>
      <Instrument>
        <longName>Tenor</longName>
        <shortName>T.</shortName>
        <trackName>Tenor</trackName>
        <minPitchP>48</minPitchP>
        <maxPitchP>72</maxPitchP>
        <minPitchA>48</minPitchA>
        <maxPitchA>69</maxPitchA>
        <instrumentId>voice.tenor</instrumentId>
        <clef>G8vb</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="0"/>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="4">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        <defaultClef>F</defaultClef>
        </Staff>
      <trackName>Bass</trackName>
      <Instrument>
        <longName>Bass</longName>
        <shortName>B.</shortName>
        <trackName>Bass</trackName>
        <minPitchP>38</minPitchP>
        <maxPitchP>62</maxPitchP>
        <minPitchA>41</minPitchA>
        <maxPitchA>60</maxPitchA>
        <instrumentId>voice.bass</instrumentId>
        <clef>F</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="0"/>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
"""

    four_choir_parts = """    <Part>
      <Staff id="1">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        <bracket type="0" span="4" col="0"/>
        </Staff>
      <trackName>Soprano</trackName>
      <Instrument>
        <longName>Soprano</longName>
        <shortName>S.</shortName>
        <trackName>Soprano</trackName>
        <minPitchP>60</minPitchP>
        <maxPitchP>84</maxPitchP>
        <minPitchA>60</minPitchA>
        <maxPitchA>79</maxPitchA>
        <instrumentId>voice.soprano</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="2">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Alto</trackName>
      <Instrument>
        <longName>Alto</longName>
        <shortName>A.</shortName>
        <trackName>Alto</trackName>
        <minPitchP>52</minPitchP>
        <maxPitchP>77</maxPitchP>
        <minPitchA>55</minPitchA>
        <maxPitchA>74</maxPitchA>
        <instrumentId>voice.alto</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="3">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        <defaultClef>G8vb</defaultClef>
        </Staff>
      <trackName>Tenor</trackName>
      <Instrument>
        <longName>Tenor</longName>
        <shortName>T.</shortName>
        <trackName>Tenor</trackName>
        <minPitchP>48</minPitchP>
        <maxPitchP>72</maxPitchP>
        <minPitchA>48</minPitchA>
        <maxPitchA>69</maxPitchA>
        <instrumentId>voice.tenor</instrumentId>
        <clef>G8vb</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="4">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        <defaultClef>F</defaultClef>
        </Staff>
      <trackName>Bass</trackName>
      <Instrument>
        <longName>Bass</longName>
        <shortName>B.</shortName>
        <trackName>Bass</trackName>
        <minPitchP>38</minPitchP>
        <maxPitchP>62</maxPitchP>
        <minPitchA>41</minPitchA>
        <maxPitchA>60</maxPitchA>
        <instrumentId>voice.bass</instrumentId>
        <clef>F</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <controller ctrl="0" value="0"/>
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
"""

    three_piano_parts = """    <Part>
      <Staff id="1">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Voice 1</trackName>
      <Instrument>
        <longName>Voice 1</longName>
        <shortName>V1.</shortName>
        <trackName>Piano</trackName>
        <minPitchP>21</minPitchP>
        <maxPitchP>108</maxPitchP>
        <minPitchA>21</minPitchA>
        <maxPitchA>108</maxPitchA>
        <instrumentId>keyboard.piano</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>95</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="2">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Voice 2</trackName>
      <Instrument>
        <longName>Voice 2</longName>
        <shortName>V2.</shortName>
        <trackName>Piano</trackName>
        <minPitchP>21</minPitchP>
        <maxPitchP>108</maxPitchP>
        <minPitchA>21</minPitchA>
        <maxPitchA>108</maxPitchA>
        <instrumentId>keyboard.piano</instrumentId>
        <clef staff="2">F</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>95</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="3">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Voice 3</trackName>
      <Instrument>
        <longName>Voice 3</longName>
        <shortName>V3.</shortName>
        <trackName>Piano</trackName>
        <minPitchP>21</minPitchP>
        <maxPitchP>108</maxPitchP>
        <minPitchA>21</minPitchA>
        <maxPitchA>108</maxPitchA>
        <instrumentId>keyboard.piano</instrumentId>
        <clef staff="2">F</clef>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>95</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel>
          <program value="0"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
"""

    three_choir_parts = """    <Part>
      <Staff id="1">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Voice 1</trackName>
      <Instrument>
        <longName>Voice 1</longName>
        <shortName>V1.</shortName>
        <trackName>Women</trackName>
        <minPitchP>55</minPitchP>
        <maxPitchP>84</maxPitchP>
        <minPitchA>55</minPitchA>
        <maxPitchA>81</maxPitchA>
        <instrumentId>voice.female</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel name="Soprano">
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        <Channel name="Alto">
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="2">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Voice 2</trackName>
      <Instrument>
        <longName>Voice 2</longName>
        <shortName>V2.</shortName>
        <trackName>Women</trackName>
        <minPitchP>55</minPitchP>
        <maxPitchP>84</maxPitchP>
        <minPitchA>55</minPitchA>
        <maxPitchA>81</maxPitchA>
        <instrumentId>voice.female</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel name="Soprano">
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        <Channel name="Alto">
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
    <Part>
      <Staff id="3">
        <StaffType group="pitched">
          <name>stdNormal</name>
          </StaffType>
        </Staff>
      <trackName>Voice 3</trackName>
      <Instrument>
        <longName>Voice 3</longName>
        <shortName>V3.</shortName>
        <trackName>Women</trackName>
        <minPitchP>55</minPitchP>
        <maxPitchP>84</maxPitchP>
        <minPitchA>55</minPitchA>
        <maxPitchA>81</maxPitchA>
        <instrumentId>voice.female</instrumentId>
        <Articulation>
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="staccatissimo">
          <velocity>100</velocity>
          <gateTime>33</gateTime>
          </Articulation>
        <Articulation name="staccato">
          <velocity>100</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="portato">
          <velocity>100</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="tenuto">
          <velocity>100</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="marcato">
          <velocity>120</velocity>
          <gateTime>67</gateTime>
          </Articulation>
        <Articulation name="sforzato">
          <velocity>150</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Articulation name="sforzatoStaccato">
          <velocity>150</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoStaccato">
          <velocity>120</velocity>
          <gateTime>50</gateTime>
          </Articulation>
        <Articulation name="marcatoTenuto">
          <velocity>120</velocity>
          <gateTime>100</gateTime>
          </Articulation>
        <Channel name="Soprano">
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        <Channel name="Alto">
          <controller ctrl="32" value="17"/>
          <program value="52"/>
          <synti>Fluid</synti>
          </Channel>
        </Instrument>
      </Part>
"""

    staff_start = """    <Staff id="{}">
"""

    vbox = """      <VBox>
        <height>10</height>
        <Text>
          <style>Title</style>
          <text>{}</text>
          </Text>
        <Text>
          <style>Subtitle</style>
          <text>{}</text>
          </Text>
        <Text>
          <style>Composer</style>
          <text>{}</text>
          </Text>
        <Text>
          <style>Lyricist</style>
          <text>{}</text>
          </Text>
        </VBox>
"""

    anacrusis = """      <Measure len="{}">
        <irregular>1</irregular>
        <voice>
"""

    measure_start = """      <Measure>
        <voice>
"""

    bass_clef = """          <Clef>
            <concertClefType>F</concertClefType>
            <transposingClefType>F</transposingClefType>
            </Clef>
"""

    key_sig = """          <KeySig>
            <accidental>{}</accidental>
            </KeySig>
"""

    time_sig = """          <TimeSig>
            <sigN>{}</sigN>
            <sigD>{}</sigD>
            </TimeSig>
"""

    time_sig_common = """          <TimeSig>
            <subtype>{}</subtype>
            <sigN>{}</sigN>
            <sigD>{}</sigD>
            </TimeSig>
"""

    tempo = """          <Tempo>
            <tempo>1.5</tempo>
            <followText>1</followText>
            <text><sym>metNoteQuarterUp</sym> = 90</text>
            </Tempo>
"""

    harmony = """          <Harmony>
            <name>{}</name>
            </Harmony>
"""

    chord_start = """          <Chord>
"""

    dots = """            <dots>{}</dots>
"""

    duration_start = """            <durationType>{}</durationType>
"""

    lyric = """            <Lyrics>
              <text>{}</text>
              </Lyrics>
"""

    note = """            <Note>
              <pitch>{}</pitch>
              <tpc>{}</tpc>
              </Note>
"""

    note_accidental = """            <Note>
              <Accidental>
                <subtype>{}</subtype>
                </Accidental>
              <pitch>{}</pitch>
              <tpc>{}</tpc>
              </Note>
"""

    chord_end = """            </Chord>
"""

    rest = """          <Rest>
            <durationType>{}</durationType>
            </Rest>
"""

    rest_dots = """          <Rest>
            <dots>{}</dots>
            <durationType>{}</durationType>
            </Rest>
"""

    measure_rest = """          <Rest>
            <durationType>measure</durationType>
            <duration>{}</duration>
            </Rest>
"""

    measure_end = """          </voice>
        </Measure>
"""

    staff_end = """      </Staff>
"""

    end = """    </Score>
  </museScore>
"""
