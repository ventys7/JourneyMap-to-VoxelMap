#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from nbtlib import File, Compound, Int, IntArray

# -----------------------------
# Configurazione cartelle
# -----------------------------
INPUT_DIR = "input"
OUTPUT_DIR = "output"
INPUT_FILE = os.path.join(INPUT_DIR, "WaypointData.dat")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "journey_from_dat.points")

# -----------------------------
# Funzioni di supporto
# -----------------------------
def sanitize(name: str) -> str:
    """Rimuove caratteri problematici dai nomi dei waypoint."""
    forbidden = [',', '#', ':']
    for c in forbidden:
        name = name.replace(c, '_')
    return name.strip()

def convert_waypoints(journey_file_path: str):
    """Legge i waypoint da JourneyMap e li converte in formato VoxelMap (.points)."""
    try:
        # il tuo file .dat non è compresso
        nbt_file = File.load(journey_file_path, gzipped=False)
    except Exception as e:
        print(f"❌ Errore nel leggere {journey_file_path}: {e}")
        return []

    waypoints_root = nbt_file.get("waypoints")
    if not waypoints_root:
        print("⚠️ Nessun waypoint trovato nella root")
        return []

    points = []

    for guid, wp in waypoints_root.items():
        if isinstance(wp, Compound):
            try:
                name = sanitize(str(wp.get("name", "unnamed")))
                pos = wp.get("pos")
                if not isinstance(pos, Compound):
                    continue
                x = int(pos.get("x", 0))
                y = int(pos.get("y", 0))
                z = int(pos.get("z", 0))
                dimension = str(wp.get("dimension", "overworld"))

                # colore
                color = wp.get("color")
                r = g = b = 1.0  # default bianco
                if isinstance(color, IntArray) and len(color) >= 3:
                    r, g, b = [color[i] / 255.0 for i in range(3)]

                points.append(
                    f"name:{name},x:{x},z:{z},y:{y},enabled:false,red:{r},green:{g},blue:{b},suffix:,world:,dimensions:{dimension}#"
                )
            except Exception as e:
                print(f"⚠️ Errore parsing waypoint {guid}: {e}")
        else:
            # alcuni oggetti nella lista dei waypoint non sono waypoint validi
            continue

    return points

# -----------------------------
# Funzione principale
# -----------------------------
def main():
    # Crea le cartelle se non esistono
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Controlla presenza file
    if not os.path.exists(INPUT_FILE):
        print(f"❌ File mancante: {INPUT_FILE}")
        return

    # Converte i waypoint
    points = convert_waypoints(INPUT_FILE)

    if not points:
        print("⚠️ Nessun waypoint valido trovato")
        return

    # Scrive il file .points
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("subworlds:\noldNorthWorlds:\nseeds:\n")
            for line in points:
                f.write(line + "\n")
        print(f"✅ Convertiti {len(points)} waypoint")
        print(f"📁 Output: {OUTPUT_FILE}")
    except Exception as e:
        print(f"❌ Errore nello scrivere {OUTPUT_FILE}: {e}")

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    main()
