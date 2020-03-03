import java.io.*;
import java.nio.file.Paths;
import java.util.Properties;

public class WSService {
    private String pythonPath;
    private WSModel model;

    public WSService() {
        model = new WSModel();

    //  получаем из конфигурационного файла путь к интерпретатору Питона
        Properties property = new Properties();
        String propertyPath = Paths.get(new File(System.getProperty("user.dir")).toString(), "resources",
                "ws.properties").toString();
        try {
            property.load(new FileInputStream(propertyPath));
        } catch (IOException e) {
            System.out.println("Конфигурационный файл не найден.");
            e.printStackTrace();
        }
        this.pythonPath = property.getProperty("python");
    }

    /**
     * Синхронизирует данные модели с данными от датчиков
     */
    private void sync() {
        // запускаем обертку над драйвером, возвращающую данные от датчиков
        String path = Paths.get(new File(System.getProperty("user.dir")).toString(), "driver", "jdriver.py").toString();
        ProcessBuilder pb = new ProcessBuilder(this.pythonPath, path);
        try {
            Process process = pb.start();
            BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String[] lines = in.readLine().toString().split(" ");
            // парсим строчку с данными от датчиков
            this.model.setLuminosity(Float.parseFloat(lines[0].split(":")[1]));
            this.model.setTemperature(Float.parseFloat(lines[1].split(":")[1]));
            this.model.setHumidity(Float.parseFloat(lines[2].split(":")[1]));
            this.model.setPressure(Float.parseFloat(lines[3].split(":")[1]));
            this.model.setAltitude(Float.parseFloat(lines[4].split(":")[1]));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * @return Модель с данными от датчиков
     */
    public WSModel getModel() {
        this.sync();
        return this.model;
    }

    public static void main(String[] args){
        WSService service = new WSService();
        service.getModel();
    }
}
