
# Use an official Java runtime as the base image
FROM openjdk:11-jre-slim

# Add the application's jar to the container
COPY target/recommendation-engine.jar /usr/app/recommendation-engine.jar

# Expose port 8080 for the service
EXPOSE 8080

# Run the jar file
ENTRYPOINT ["java", "-jar", "/usr/app/recommendation-engine.jar"]
