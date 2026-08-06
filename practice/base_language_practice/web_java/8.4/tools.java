import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class FileOrganizer {

    // 配置要整理的文件夹路径（改成你自己的路径）
    private static final String TARGET_DIR = "D:/下载";

    // 配置分类规则：扩展名 → 子文件夹名
    private static final String[][] RULES = {
            {"pdf", "PDF文件"},
            {"doc", "文档"},
            {"docx", "文档"},
            {"txt", "文档"},
            {"jpg", "图片"},
            {"jpeg", "图片"},
            {"png", "图片"},
            {"gif", "图片"},
            {"mp4", "视频"},
            {"avi", "视频"},
            {"mkv", "视频"},
            {"mp3", "音乐"},
            {"wav", "音乐"},
            {"zip", "压缩包"},
            {"rar", "压缩包"},
            {"7z", "压缩包"},
            {"exe", "安装包"},
            {"msi", "安装包"}
    };

    public static void main(String[] args) {
        File dir = new File(TARGET_DIR);

        if (!dir.exists() || !dir.isDirectory()) {
            System.out.println("目标文件夹不存在或不是文件夹: " + TARGET_DIR);
            return;
        }

        File[] files = dir.listFiles();
        if (files == null) {
            System.out.println("无法读取文件夹内容");
            return;
        }

        int movedCount = 0;
        int skippedCount = 0;

        for (File file : files) {
            // 跳过文件夹本身（只处理文件，不处理子文件夹）
            if (file.isDirectory()) {
                continue;
            }

            String fileName = file.getName();
            String extension = getExtension(fileName);

            if (extension == null) {
                System.out.println("跳过: " + fileName + "（无扩展名）");
                skippedCount++;
                continue;
            }

            String targetFolderName = getTargetFolder(extension);
            if (targetFolderName == null) {
                System.out.println("跳过: " + fileName + "（未识别的扩展名: " + extension + "）");
                skippedCount++;
                continue;
            }

            // 构建目标文件夹路径
            File targetDir = new File(TARGET_DIR + "/" + targetFolderName);
            if (!targetDir.exists()) {
                targetDir.mkdirs(); // 创建文件夹
            }

            // 移动文件
            File targetFile = new File(targetDir, fileName);

            // 如果目标位置已有同名文件，添加序号避免覆盖
            int counter = 1;
            while (targetFile.exists()) {
                String baseName = fileName.substring(0, fileName.lastIndexOf('.'));
                String ext = fileName.substring(fileName.lastIndexOf('.'));
                targetFile = new File(targetDir, baseName + "_" + counter + ext);
                counter++;
            }

            boolean success = file.renameTo(targetFile);
            if (success) {
                System.out.println("已移动: " + fileName + " → " + targetFolderName);
                movedCount++;
            } else {
                // 如果 renameTo 失败，尝试用 Files.move（更可靠）
                try {
                    Path sourcePath = file.toPath();
                    Path targetPath = targetFile.toPath();
                    Files.move(sourcePath, targetPath);
                    System.out.println("已移动(Java NIO): " + fileName + " → " + targetFolderName);
                    movedCount++;
                } catch (IOException e) {
                    System.err.println("移动失败: " + fileName + "，错误: " + e.getMessage());
                    skippedCount++;
                }
            }
        }

        System.out.println("\n整理完成！");
        System.out.println("已移动: " + movedCount + " 个文件");
        System.out.println("已跳过: " + skippedCount + " 个文件");
    }

    // 获取文件的扩展名（小写）
    private static String getExtension(String fileName) {
        int dotIndex = fileName.lastIndexOf('.');
        if (dotIndex == -1 || dotIndex == fileName.length() - 1) {
            return null;
        }
        return fileName.substring(dotIndex + 1).toLowerCase();
    }

    // 根据扩展名查找对应的目标文件夹
    private static String getTargetFolder(String extension) {
        for (String[] rule : RULES) {
            if (rule[0].equals(extension)) {
                return rule[1];
            }
        }
        return null;
    }
}