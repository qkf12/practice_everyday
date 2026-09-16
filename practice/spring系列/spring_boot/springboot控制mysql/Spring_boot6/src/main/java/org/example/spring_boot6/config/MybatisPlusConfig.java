package org.example.spring_boot6.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;

@MapperScan("org.example.spring_boot6.mapper")
@Configuration
public class MybatisPlusConfig {
}
