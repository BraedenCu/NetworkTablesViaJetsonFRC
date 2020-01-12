
/**SHoutout
  * TO
  * DRAKON
  * Michael
  * For making this
  */

package frc.robot;

import com.ctre.phoenix.motorcontrol.ControlMode;
import com.ctre.phoenix.motorcontrol.can.TalonSRX;
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.GenericHID.RumbleType;
import edu.wpi.first.wpilibj.PowerDistributionPanel;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.TimedRobot;
import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.Map;

/**
 * The VM is configured to automatically run this class, and to call the
 * functions corresponding to each mode, as described in the TimedRobot
 * documentation. If you change the name of this class or the package after
 * creating this project, you must also update the manifest file in the resource
 * directory.
 */
public class Robot extends TimedRobot {


  private int JoystickPort = 0;
  @Override
  public void robotInit() {
    PDP.clearStickyFaults();

    // Set up input map
    inputMap.put("leftX", 0);
    inputMap.put("leftY", 1);
    inputMap.put("rightX", 4);
    inputMap.put("rightY", 5);

    // Set up networktables
    NetworkTableInstance tableInstance = NetworkTableInstance.getDefault();
    NetworkTable table = tableInstance.getTable("datatable");
    dataEntry = table.getEntry("X");
    System.out.println("\n---ROBOT INITIATED---\n\n Begin Log:\n\n\n");
  }

  /**
   * This function is run once each time the robot enters autonomous mode.
   */
  @Override
  public void autonomousInit() {
    System.out.println("\n---SETTING UP AUTONOMOUS---\n");
    // START CODE HERE
    m_timer.reset();
    m_timer.start();
    // END CODE HERE
    System.out.println("\n---AUTONOMOUS INITIATED---\n");
  }

  @Override
  public void autonomousPeriodic() {

  }

  /**
   * This function is called once each time the robot enters teleoperated mode.
   */
  @Override
  public void teleopInit() {
    
  }

  /**
   * This function is called periodically during teleoperated mode.
   */
  @Override
  public void teleopPeriodic() {

      if (driverControlJoystick.getRawButtonPressed(3) == true) {
        dataEntry.setNumber(1);
        System.out.println("Sent Blue Data");
      } else if (driverControlJoystick.getRawButtonPressed(4) == true) {
        dataEntry.setNumber(2);
      }

      System.out.println(dataEntry.getNumber(0));
    }

  }

