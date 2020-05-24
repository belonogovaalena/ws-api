package jweatherstation;

import jweatherstation.WSDriver;
import jweatherstation.WSModel;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class WSService {
    private WSModel model;
    private WSDriver driver;

    public WSService() {
        this.model = new WSModel();
        this.driver = new WSDriver();
        driver.startUp();
    }

    public String getLine() {
        return driver.getLine();
    }

    public void processLine() {
        String text = getLine();
        if (text == null || text.isEmpty()) {
            return;
        }
        Pattern humidityPattern1 = Pattern.compile("Влажность:([\\d\\.]*)%");
        Pattern temperaturePattern1 = Pattern.compile("Температура:([\\d\\.]*)°C");
        Pattern luminosityPattern1 = Pattern.compile("Свет:([-\\d\\.]*) lux");
        Pattern pressurePattern1 = Pattern.compile("Давление:([\\d\\.]*)мм.рт.ст.");
        Pattern altitudePattern1 = Pattern.compile("Высота:([-\\d\\.]*)м");
        Matcher humidityMatcher = humidityPattern1.matcher(text);
        Matcher temperatureMatcher = temperaturePattern1.matcher(text);
        Matcher luminosityMatcher = luminosityPattern1.matcher(text);
        Matcher pressureMatcher = pressurePattern1.matcher(text);
        Matcher altitudeMatcher = altitudePattern1.matcher(text);
        if (humidityMatcher.find()) {
            this.model.setHumidity(Float.parseFloat(humidityMatcher.group(1)));
        } else if (temperatureMatcher.find()) {
            this.model.setTemperature(Float.parseFloat(temperatureMatcher.group(1)));
        } else if (luminosityMatcher.find()) {
            this.model.setLuminosity(Float.parseFloat(luminosityMatcher.group(1)));
        } else if (pressureMatcher.find()) {
            this.model.setPressure(Float.parseFloat(pressureMatcher.group(1)));
        } else if (altitudeMatcher.find()) {
            this.model.setAltitude(Float.parseFloat(altitudeMatcher.group(1)));
        }

        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public WSModel getModel() {
        return model;
    }

    public static void main(String[] args) {
        WSService s = new WSService();
        while (true) {
            s.processLine();
            System.out.println(s.getModel().toString());
        }
    }
}
