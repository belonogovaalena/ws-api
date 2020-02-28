package weatherstation;

public class WSModel {
    private float altitude;
    private float humidity;
    private float luminosity;
    private float pressure;
    private float temperature;

    public WSModel() {}

    /**
     * @param altitude Высота точки измерения относительно места установки метеостанции, м
     * @param humidity Относительная влажность, %
     * @param luminosity Уровень освещенности, люмен
     * @param pressure Давление, мм.рт.ст
     * @param temperature Температура, *С
     */
    public WSModel(float altitude, float humidity, float luminosity, float pressure, float temperature) {
        this.altitude = altitude;
        this.humidity = humidity;
        this.luminosity = luminosity;
        this.pressure = pressure;
        this.temperature = temperature;
    }

    /**
     * @return Высота точки измерения относительно места установки метеостанции, м
     */
    public float getAltitude() {
        return this.altitude;
    }

    /**
     * @return Относительная влажность, %
     */
    public float getHumidity() {
        return this.humidity;
    }

    /**
     * @return Уровень освещенности, люмен
     */
    public float getLuminosity() {
        return this.luminosity;
    }

    /**
     * @return Давление, мм.рт.ст
     */
    public float getPressure() {
        return this.pressure;
    }

    /**
     * @return Температура, *С
     */
    public float getTemperature() {
        return temperature;
    }

    /**
     * @param altitude Высота точки измерения относительно места установки метеостанции, м
     */
    public void setAltitude(float altitude) {
        this.altitude = altitude;
    }

    /**
     * @param humidity Относительная влажность, %
     */
    public void setHumidity(float humidity) {
        this.humidity = humidity;
    }

    /**
     * @param luminosity Уровень освещенности, люмен
     */
    public void setLuminosity(float luminosity) {
        this.luminosity = luminosity;
    }

    /**
     * @param pressure Давление, мм.рт.ст
     */
    public void setPressure(float pressure) {
        this.pressure = pressure;
    }

    /**
     * @param temperature Температура, *С
     */
    public void setTemperature(float temperature) {
        this.temperature = temperature;
    }
}
