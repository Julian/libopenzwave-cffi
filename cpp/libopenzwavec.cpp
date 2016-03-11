#include "libopenzwavec.h"

#include "openzwave/Options.h"


int main() {}


extern "C"
{
    COptions newCOptions(
            const char *cConfigPath,
            const char *cUserPath,
            const char *cCommandLine
            )
    {
        std::string configPath = cConfigPath;
        std::string userPath = cUserPath;
        std::string commandLine = cCommandLine;
        return reinterpret_cast<void*>(
                OpenZWave::Options::Create(configPath, userPath, commandLine));
    }
}
