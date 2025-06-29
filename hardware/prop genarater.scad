//Multipropv6.scad
//This variation includes the chord length relationship and pitch as a parameter
//This variation treats it as a standard propellor.
//v2 Trims the blade stub to make it merge better for small numbers of blades
//v3 Fixes problems with the Blade width function not being adjusted for length
      //of blade
//v4 No changes to the code other than introducing an ability to change
// the hub core cut-out cone shape and change to different default values.
//v5 Airfoil_points variable used instead to allow easier substitution of other airfoils.
//v6 Some extra holes added to the hub to allow hubs with extra pins to be designed.

// Points from naca4412.dat in the archive: http://m-selig.ae.illinois.edu/ads/archives/coord_seligFmt.tar.gz
// Not necessarily in the same order as in: http://m-selig.ae.illinois.edu/ads/coord/naca4412.dat

PitchI = 4.5;    //pitch (inches)
DiamI = 9;     //diameter (inches)
BladeNo = 3;    //Number of blades

PitchM = 0;    //pitch (mm)
DiamM = 0;     //diameter (mm)

MaxChdW = 19;   //Maximum chord length

Statns = 10;    //No of stations to calculate the chord length and twist
SectRes = 10;   //Resolution of the steps within each section.  

Pitch = (PitchM > 0)? (PitchM):(PitchI * 25.4);  //Turn pitch values into metric
Diam = (DiamM > 0)? (DiamM):(DiamI * 25.4);  //Turn pitch values into metric

PitchAdjHub = 1;  //Adjustment factor for pitch angle for hub end.
PitchAdjTip = 1;  //Adjustment factor for pitch angle for tip end.

BldCtr = 35;    //% of chord width where centre of blade is.

PropShftD = 5;  //Propellor shaft hole size
PropHubD = 10; //Propellor hub diameter
PropHubDCutterMax = 14; //Maximum diameter of the Hub cone cutter
PropHubT = 5;   //Propellor hub thickness

//Hub pin option (if left as 0, then this option will be ignored)
HubPinD = 0;  //Diameter of pins
HubPinPCD = 0;  //Pitch circle diameter for location of the Hub Pins.

//Holder variables for blade section calculations.
Poz1 =0;
Poz2 = 0;  //Positions for ends of each section
 //Holder variables for calculated Blade section parameters
StrtAngi = 0;
EndAngi = 0;
StepLi = 0;
StrtWi = 0;
EndWi = 0; 


// Blade airfoil profile.  Replace this as needed. 
Airfoil_points = [[1000,1.3],[950,14.7],[900,27.1],[800,48.9],[700,66.9],[600,81.4],[500,91.9],[400,98],[300,97.6],[250,94.1],[200,88],[150,78.9],[100,65.9],[75,57.6],[50,47.3],[25,33.9],[12.5,24.4],[0,0],[12.5,-14.3],[25,-19.5],[50,-24.9],[75,-27.4],[100,-28.6],[150,-28.8],[200,-27.4],[250,-25],[300,-22.6],[400,-18],[500,-14],[600,-10],[700,-6.5],[800,-3.9],[900,-2.2],[950,-1.6],[1000,-1.3]];  // Naca4412 Airfoil

//The following blade width shape is a function taken from an existing blade.
//It should be varied with other functions to suit the needs to the user.
//The variable is a ratio of the position along the blade length.
function BldChrdLen(x) = 1.392*pow(x,4) -1.570*pow(x,3)-2.46*pow(x,2)+3.012*x+0.215;

SectL =  Diam/(2*Statns);  //Length of each section

//Number of steps in the Stub section /This will be calculated for 1/6th of
//blade length or 1.5 * Hub diameter, whichever is bigger
StubSteps = (Diam/(12*SectL)>PropHubD*1.5)?round(Diam/(12*SectL)):round(PropHubD*1.5/SectL);

BldStubLn = 0.98*StubSteps * SectL;  //The length of the hub section of blade 
//To ensure a manifold join we will reduce the stub length a tiny amount

//Function to adjust the pitch angle to match manufactured blades (which are flatter)
function PitchAngAdj(x) = 2*(PitchAdjTip-PitchAdjHub)/Diam*x+PitchAdjHub;


module hub()
{
    translate([0,0,-0.25*PropHubT])cylinder (r = PropHubD/2, h = 1.5*PropHubT, center = true, $fn = 100);
}

module Hubcutter()
{
    union()
    {
        cylinder (r = PropShftD/2, h = PropHubT*1.5, center = true, $fn = 100);
        translate([0,0,-1.5*PropHubT])cylinder (r2 = PropHubD/2, r1 = 0.5*PropHubDCutterMax, h = 2*PropHubT, center = true, $fn = 100);
        
        //Hub pin option.  If the HubPinD and HubPinPCD parameters
        //Are zero, the option will be ignored.
        
        if(HubPinD > 0 && HubPinPCD > 0)
        {
            translate([0.5*HubPinPCD,0,0])cylinder(r = 0.5*HubPinD, h = PropHubT*1.5, center = true, $fn = 100);
            translate([-0.5*HubPinPCD,0,0])cylinder(r = 0.5*HubPinD, h = PropHubT*1.5, center = true, $fn = 100);
        }
    }
}

module Bladeprofile(StrtAng, EndAng, StepL, StrtW, EndW)
//Parameters being parsed are Start Angle, End Angle, The height of the section
// the start chord length and the end chord length.
{
    echo(StrtAng, EndAng, StepL, StrtW, EndW);
    linear_extrude(height=StepL, scale=EndW/StrtW,twist = EndAng - StrtAng, slices = SectRes)
     rotate([0,0,-StrtAng])  //Position angle
     translate([-BldCtr/100*StrtW,0])  //shift profile to position airfoil centreline
     scale(StrtW) //Base Scale at start
     scale (0.001) polygon(points=Airfoil_points); //Scale profile to unit size)
    
}

module BladeBuilder()
{
    //Step through the sections defined by the number of stations and 
    //Add a section of blade profile.
    union()
    {
    for(i = [0:Statns-1])
        {
            //calculate the position start and end variables
            // for the particular section
            Poz1 = i*SectL; 
            Poz2 = (i+1)*SectL;
            
            //calculate the chord lengths at the two positions
            StrtWi = BldChrdLen(2*Poz1/Diam)*MaxChdW;
            EndWi = BldChrdLen(2*Poz2/Diam)*MaxChdW;
            
            //calculate the blade angles at the two positions
            StrtAngi = atan(Pitch/(2*PI*Poz1))*PitchAngAdj(Poz1);
            EndAngi = atan(Pitch/(2*PI*Poz2))*PitchAngAdj(Poz2);
            
            translate([0,0,Poz1])Bladeprofile(StrtAngi, EndAngi,SectL,StrtWi, EndWi);
           
            
        }
    }
}

module CoreBit()
{
    //To strengthen the rotor core we'll use a stub of blade and 
    //the section of the hub to create a hull shape that should
   //merge it tidily.
    hull()
    {
       hub();
       //Blade stub - Width to merge with main blade
       EndWi = BldChrdLen(2*BldStubLn/Diam)*MaxChdW;
       
        //Blade stub angles and twist.
        StrtAngi = PitchAngAdj(0.5*PropHubD);
        EndAngi = atan(Pitch/(2*PI*BldStubLn))*PitchAngAdj(BldStubLn);
        
        difference()
        {
        rotate([90,0,0])Bladeprofile(StrtAngi, EndAngi, BldStubLn, EndWi, EndWi);
            union(){
            //Add some cutters to trim the blade stub to make a tidier merge for
            //small numbers of blades.
                rotate([0,0,15])
                translate([0.5*(PropHubD+EndWi),-0.5*BldStubLn,0])
                cube([EndWi,BldStubLn,EndWi],center = true);
                
                rotate([0,0,-15])
                translate([-0.5*(PropHubD+EndWi),-0.5*BldStubLn,0])
                cube([EndWi,BldStubLn,EndWi],center = true);   
            }
        }
    }
}



difference()
{
    union()
    {
        
        for(N = [0:BladeNo-1])
        {
            rotate([90,0,N*360/BladeNo])BladeBuilder();
             rotate([0,0,N*360/BladeNo])CoreBit();
        }
    }
    Hubcutter();
}
