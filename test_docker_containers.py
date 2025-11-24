import subprocess
import json
import sys

def check_docker_containers():
    """Check if Docker containers are running properly"""
    print(" Checking Docker Containers...")
    print("=" * 50)
    
    try:
        # Check if containers are running
        result = subprocess.run(
            ["docker", "compose", "ps", "--format", "json"],
            capture_output=True, text=True, timeout=30
        )
        
        if result.returncode != 0:
            print(" Failed to check Docker containers")
            print(f"Error: {result.stderr}")
            return False
        
        # Parse the JSON output
        containers = json.loads(result.stdout)
        
        print(" Running Containers:")
        all_healthy = True
        
        for container in containers:
            name = container.get("Name", "Unknown")
            service = container.get("Service", "Unknown")
            status = container.get("Status", "Unknown")
            state = container.get("State", "Unknown")
            
            print(f"   {service}:")
            print(f"     - Name: {name}")
            print(f"     - Status: {status}")
            print(f"     - State: {state}")
            
            if "healthy" in status.lower() or state == "running":
                print(f"     -  Healthy")
            else:
                print(f"     -  Issues detected")
                all_healthy = False
        
        # Check specific ports
        print("\n Checking Ports:")
        ports_to_check = [5432, 8080]
        for port in ports_to_check:
            result = subprocess.run(
                ["netstat", "-an"],  # Windows
                # ["ss", "-tuln"],   # Linux alternative
                # ["lsof", "-i", f":{port}"],  # Mac alternative
                capture_output=True, text=True
            )
            if str(port) in result.stdout:
                print(f"   Port {port}:  In use")
            else:
                print(f"   Port {port}:  Not in use")
        
        return all_healthy
        
    except subprocess.TimeoutExpired:
        print(" Docker command timed out")
        return False
    except json.JSONDecodeError:
        print(" Failed to parse Docker output")
        return False
    except Exception as e:
        print(f" Error checking Docker: {e}")
        return False

def test_container_connectivity():
    """Test if we can connect to the containers"""
    print("\n Testing Container Connectivity...")
    
    # Test PostgreSQL connection by trying to run a command inside container
    try:
        result = subprocess.run([
            "docker", "exec", "resume_postgres", 
            "pg_isready", "-U", "postgres", "-h", "localhost"
        ], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print(" PostgreSQL container is accepting connections")
        else:
            print(" PostgreSQL container not ready")
            print(f"Output: {result.stdout}")
            return False
            
    except Exception as e:
        print(f" Failed to test PostgreSQL container: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print(" Docker Container Health Check")
    print("=" * 50)
    
    containers_ok = check_docker_containers()
    connectivity_ok = test_container_connectivity()
    
    if containers_ok and connectivity_ok:
        print("\n ALL DOCKER CHECKS PASSED!")
        print("Containers are running and healthy")
    else:
        print("\n Some Docker checks failed")
        sys.exit(1)